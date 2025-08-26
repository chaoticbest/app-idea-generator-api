from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from generate import generate_idea, AppIdea
import json
from datetime import datetime

app = FastAPI(title="App Idea Generator API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Category mapping from snake_case to display names
CATEGORY_MAPPING = {
    "generative-visuals-ambience": "Generative Visuals & Ambience",
    "audio-music": "Audio & Music",
    "productivity-time": "Productivity & Time",
    "writing-language": "Writing & Language",
    "wellness-mood": "Wellness & Mood",
    "social-playful": "Social & Playful",
    "data-and-vizualization": "Data and Vizualization",
    "web-readers-scrapers-linkers": "Web Readers, Scrapers & Linkers",
    "games-toys": "Games & Toys",
    "developer-and-creative-utiltiies": "Developer and Creative Utiltiies",
    "retro-web": "Retro Web",
    "printables": "Printables",
    "learning-studying": "Learning & Studying",
    "accessibility": "Accessibility",
    "color-type-layout": "Color, Type & Layout",
    "camera-visual-effects": "Camera & Visual Effects",
    "marketing": "Marketing",
    "personal-finance": "Personal Finance",
    "maps-places-journeys": "Maps, Places & Journeys",
    "collaboration": "Collaboration"
}

@app.get("/")
async def root():
    """Root endpoint with API information"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== API Info Request [{timestamp}] ===")
    print("Root endpoint accessed")
    print("=" * 40)
    return {
        "message": "App Idea Generator API",
        "version": "1.0.0",
        "endpoints": {
            "/generate": "GET - Generate app ideas for a category",
            "/categories": "GET - List all available categories"
        }
    }

@app.get("/categories")
async def get_categories():
    """Get all available categories"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== Categories Request [{timestamp}] ===")
    print("Categories endpoint accessed")
    print(f"Available categories: {len(CATEGORY_MAPPING)}")
    print("=" * 40)
    return {
        "categories": list(CATEGORY_MAPPING.keys()),
        "display_names": list(CATEGORY_MAPPING.values())
    }

@app.get("/generate")
async def generate_app_idea(c: str = Query(..., description="Category in snake_case format")):
    """
    Generate app ideas for a specific category.
    
    Args:
        c: Category in snake_case format (e.g., 'generative-visuals-ambience')
    
    Returns:
        AppIdea object with name and description
    """
    # Validate category
    if c not in CATEGORY_MAPPING:
        available_categories = list(CATEGORY_MAPPING.keys())
        error_msg = f"Invalid category '{c}'. Available categories: {available_categories}"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n=== INVALID CATEGORY REQUEST [{timestamp}] ===")
        print(f"Requested category: '{c}'")
        print(f"Available categories: {available_categories}")
        print("=" * 50)
        raise HTTPException(
            status_code=400, 
            detail=error_msg
        )
    
    # Get the display name for the category
    category_display_name = CATEGORY_MAPPING[c]
    
    try:
        # Generate the app idea using the existing function
        app_idea = await generate_idea(category_display_name)
        
        # Print the result to terminal before sending to client
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n=== Generated App Idea for '{category_display_name}' [{timestamp}] ===")
        print(f"Name: {app_idea.name}")
        print(f"Description: {app_idea.description}")
        print("=" * 60)
        
        return app_idea
    except Exception as e:
        error_msg = f"Error generating app idea: {str(e)}"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n=== ERROR for '{category_display_name}' [{timestamp}] ===")
        print(error_msg)
        print("=" * 60)
        raise HTTPException(
            status_code=500,
            detail=error_msg
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
