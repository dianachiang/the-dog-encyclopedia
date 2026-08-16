def get_dog_breed(breed_name):
    """Fetch dog breed information from API-Ninjas"""
    if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
        return {"error": "Please set your API key first!"}
    
    url = "https://api.api-ninjas.com/v1/dogs"
    headers = {'X-Api-Key': API_KEY}
    
    try:
        response = requests.get(url, params={'name': doberman}, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]
            else:
                return {"error": f"No breed found for '{doberman}'"}
        else:
            return {"error": f"API Error: {response.status_code}"}
    except Exception as e:
        return {"error": f"Connection error: {str(e)}"}
