from typing import Any, Optional
from django.core.management.base import BaseCommand
from battery_backed.models import StateOfCharge
from datetime import datetime
from pytz import timezone
import paho.mqtt.client as mqtt
import json


class Command(BaseCommand):
    help = 'MQTT Processing'

    def validate_json(self, json_data: str) -> bool:
        try:
            json.loads(json_data)
            return True
        except ValueError:
            return False
        
    def handle(self, *args: Any, **options: Any) -> Optional[str]:   

        def on_connect(client, userdata, flags, rc):           
            if rc == 0:
                print("Connected successfully")
                client.subscribe("battery_scada")
            else:
                print(f"Connection failed with code {rc}")

        def on_message(client, userdata, msg):            
            topic = msg.topic
            print(f"Received message on topic: {topic}")
            
            # Assuming payload is already a dictionary-like object (not a JSON string)
            try:
                payload_str = msg.payload.decode()  # Decode bytes to string
                

                # Check if payload looks like a dictionary in string form, if so, evaluate it
                # Use `json.loads()` if it was a JSON-encoded string, but seems like it's Python serialized.
                # If it is indeed a dictionary-like payload, use `eval()`, but be careful with it!
                data_out = eval(payload_str)  # In a safe environment, consider using literal_eval from ast
                print(f"Evaluated payload: {data_out}")

                if isinstance(data_out, dict):                    
                    soc = data_out.get('SoC', None)
                    first_key, first_value = next(iter(data_out.items()))
                    battery_current_status = first_key
                    battery_invertor_power = first_value

                    if soc is not None and battery_current_status is not None and battery_invertor_power is not None:
                        # now = datetime.now(timezone('Europe/London')).replace(second=0, microsecond=0) #minute resolution
                        # print(f"{now},{soc},{battery_current_status},{battery_invertor_power}")
                        
                        battery = StateOfCharge(                             
                            state_of_charge=soc, 
                            current_status= battery_current_status, 
                            invertor_power= battery_invertor_power
                        )
                        print(battery)
                        battery.save()


            except Exception as e:
                print(f"Error processing the payload: {e}")

                  
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect("159.89.103.242", 1883)        

        client.loop_forever()