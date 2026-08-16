#!/usr/bin/env python3
"""
🐕 The Dog Encyclopedia 

"""

# This project was created with the help of AI. 
# I used AI to help fix bugs in the codes when I run into error messages.
# I consulted AI to help materialize my ideas using concepts and skills not convered in class. 
# In particular, AI was used to help with the coding that brought the displays and images to life.

 

import requests
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# ============================================
# API Key Configuration
# ============================================
API_KEY = os.getenv("API_KEY")

def get_api_key():
    """Get API key from environment or prompt user"""
    global API_KEY
    if not API_KEY:
        print("\n⚠️  No API key found in environment variables.")
        print("Get a free API key at: https://api-ninjas.com/")
        API_KEY = input("Enter your API-Ninjas API key: ").strip()
        if not API_KEY:
            print("❌ No API key provided. Exiting.")
            sys.exit(1)
    return API_KEY

# ============================================
# API Functions 
# ============================================
# AI was consulted in structuring the below messages to prompt users for API KEYS.

def get_dog_breed(breed_name):
    """Fetch dog breed information from API-Ninjas"""
    if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
        return {"error": "Please set your API key first!"}
    
    url = "https://api.api-ninjas.com/v1/dogs"
    headers = {'X-Api-Key': API_KEY}
    
    try:
        response = requests.get(url, params={'name': breed_name}, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]
            else:
                return {"error": f"No breed found for '{breed_name}'"}
        else:
            return {"error": f"API Error: {response.status_code}"}
    except Exception as e:
        return {"error": f"Connection error: {str(e)}"}

# ============================================
# Display Functions 
# ============================================
# AI was consulted in creating the code for the displays. In particular, AI was used to generate the emojis.


def display_breed_info(breed_data):
    """Display complete breed information in terminal"""
    if not breed_data or "error" in breed_data:
        print(f"\n❌ {breed_data.get('error', 'No data')}")
        return
    
    print("\n" + "="*70)
    print(f"🐕 {breed_data.get('name', 'Unknown')}")
    print("="*70)
    
    # ============================================
    # Physical Characteristics
    # ============================================
    print("\n📏 SIZE & WEIGHT")
    print("-" * 40)
    
    # Height
    min_height = breed_data.get('min_height_male') or breed_data.get('min_height')
    max_height = breed_data.get('max_height_male') or breed_data.get('max_height')
    if min_height and max_height:
        print(f"  📐 Height:   {min_height} - {max_height} cm")
    
    # Weight
    min_weight = breed_data.get('min_weight_male') or breed_data.get('min_weight')
    max_weight = breed_data.get('max_weight_male') or breed_data.get('max_weight')
    if min_weight and max_weight:
        print(f"  ⚖️ Weight:   {min_weight} - {max_weight} kg")
    
    # Lifespan
    min_life = breed_data.get('min_life_expectancy')
    max_life = breed_data.get('max_life_expectancy')
    if min_life and max_life:
        print(f"  📅 Lifespan: {min_life} - {max_life} years")
    
    # ============================================
    # Trait Ratings 
    # ============================================
    print("\n⭐ TRAIT RATINGS (1-5 scale)")
    print("-" * 40)
    
    rating_fields = [
        ('👶 Good with Children', 'good_with_children'),
        ('🐕 Good with Other Dogs', 'good_with_other_dogs'),
        ('👤 Good with Strangers', 'good_with_strangers'),
        ('🎾 Playfulness', 'playfulness'),
        ('🧠 Trainability', 'trainability'),
        ('🛡️ Protectiveness', 'protectiveness'),
        ('⚡ Energy Level', 'energy'),
        ('💇 Grooming Needs', 'grooming'),
        ('💧 Drooling', 'drooling'),
        ('🗣️ Barking', 'barking'),
        ('🧹 Shedding', 'shedding'),
        ('🧥 Coat Length', 'coat_length'),
    ]
    
    for label, key in rating_fields:
        value = breed_data.get(key)
        if value is not None:
            # Visual rating bar
            filled = '█' * int(value)
            empty = '░' * (5 - int(value))
            print(f"  {label:25} {value}/5 {filled}{empty}")
        else:
            print(f"  {label:25} Not available")
    
    # ============================================
    # Image URL
    # ============================================
    image_url = breed_data.get('image_link') or breed_data.get('image')
    if image_url:
        print("\n📸 IMAGE")
        print("-" * 40)
        print(f"  {image_url}")
        print("  (Open this URL in your browser to see the image)")
    
    print("\n" + "="*70 + "\n")

# ============================================
# Interactive App 
# ============================================

def create_app():
    """Interactive terminal application"""
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║     🐕  THE DOG ENCYCLOPEDIA  🐕                          ║
    ║                                                            ║
    ║     Search for any breed to learn about your               ║
    ║     new furry friends!                                     ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    # AI was consulted in creating the above image

    # Get API key if not set
    if not API_KEY:
        get_api_key()
    print("✅ API Key loaded successfully!\n")
    
    while True:
        print("\n" + "-"*50)
        print("Options:")
        print("  [1] 🔍 Search for a dog breed")
        print("  [2] ❌ Exit")
        print("-"*50)
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "2" or choice.lower() == "exit":
            print("\n🐕 Thank you for using The Dog Encyclopedia!")
            print("👋 Goodbye!\n")
            break
        
        if choice == "1":
            breed = input("\n🐕 Enter breed name (e.g., Golden Retriever): ").strip()
            
            if not breed:
                print("⚠️  Please enter a breed name.")
                continue
            
            print(f"\n🔍 Searching for '{breed}'...")
            result = get_dog_breed(breed)
            display_breed_info(result)
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")



# ============================================
# RUN THE APP
# ============================================

if __name__ == "__main__":
    
        create_app()