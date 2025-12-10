import requests
import subprocess

def get_weather_data(city):
    #Feteches weather data for a specfic city using WeatherApi
    api_key = ''
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(base_url)
    data = response.json()

    if 'error' not in data:
        weather = data['current']['condition']['text']
        temp_c = data['current']['temp_c']

        if "Heavy rain" in weather:
            print("Weather Condition is heavy rain scaling the number of pods in AKS")
            scaleaks_pods_using_kubectl(namespace='blogging-app',deployment_name='bankapp', replicas=3)
        else:
            print("Weather condition is not heavy rain.No scaling action is required.")
    else:
        print(f"Error fetching data for {city}: {data['error']['message']}")


def scaleaks_pods_using_kubectl(namespace,deployment_name,replicas):
    #Scales the number of pods for a specific deployment using kubectl
    try:
        #run the kubectl command to scale the pods
        subprocess.run([
           'kubectl', 'scale', f'deployment/{deployment_name}', f'--replicas={replicas}',
             '-n',namespace
        ],check=True)
        print(f"Scaled the deployment {deployment_name} to {replicas} pods.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to scale pods: {e}")

get_weather_data('London')

