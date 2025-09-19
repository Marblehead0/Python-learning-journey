import argparse, sys
import requests

BASE = "https://api.open-meteo.com/v1/forecast"

def get_weather(lat: float, lon:float) -> dict:
    try:
        r = requests.get(
            BASE,
            params={"latitude": lat, "longitude": lon,"current_weather": True},
            timeout=10
        )
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        print(f"Error: {e}",file=sys.stderr)
        return{}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Current weather via Open-Meteo")
    p.add_argument("--lat",type=float, required=True)
    p.add_argument("--lon",type=float, required=True)
    p.add_argument("--units",type=str, required=False)
    args = p.parse_args()

    data = get_weather(args.lat, args.lon)
    cw = data.get("current_weather") or {}



    if cw:
            if args.units == "imperial":
                temp = (float(cw.get('temperature')) * 9/5) + 32
                speed = float(cw.get('windspeed')) / 1.609344
                print(f"Temp: {temp:.2f}°F, Wind: {speed:.2f} mph")
                
            elif args.units == "metric":
                 print(f"Temp: {cw.get('temperature')}°C, Wind: {cw.get('windspeed')} km/h")
            else:
                 print("Invalid unit argument please use 'metric' or 'imperial'")
    else:
        print("No weather data")