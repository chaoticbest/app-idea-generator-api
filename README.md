# App Idea Generator API

A FastAPI application that generates creative app ideas for different categories using OpenAI's agents.

## Features

- **GET `/`** - API information and available endpoints
- **GET `/categories`** - List all available categories
- **GET `/generate`** - Generate app ideas for a specific category

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the server

```bash
python main.py
```

The server will run on `http://localhost:5000`

### API Endpoints

#### Get API Information

```bash
curl http://localhost:5000/
```

#### List Categories

```bash
curl http://localhost:5000/categories
```

#### Generate App Idea

```bash
curl "http://localhost:5000/generate?c=generative-visuals-ambience"
```

### Available Categories

The API supports the following categories (use snake_case format):

- `generative-visuals-ambience` - Generative Visuals & Ambience
- `audio-music` - Audio & Music
- `productivity-time` - Productivity & Time
- `writing-language` - Writing & Language
- `wellness-mood` - Wellness & Mood
- `social-playful` - Social & Playful
- `data-and-vizualization` - Data and Vizualization
- `web-readers-scrapers-linkers` - Web Readers, Scrapers & Linkers
- `games-toys` - Games & Toys
- `developer-and-creative-utiltiies` - Developer and Creative Utiltiies
- `retro-web` - Retro Web
- `printables` - Printables
- `learning-studying` - Learning & Studying
- `accessibility` - Accessibility
- `color-type-layout` - Color, Type & Layout
- `camera-visual-effects` - Camera & Visual Effects
- `marketing` - Marketing
- `personal-finance` - Personal Finance
- `maps-places-journeys` - Maps, Places & Journeys
- `collaboration` - Collaboration

### Response Format

The `/generate` endpoint returns a JSON object with the following structure:

```json
{
  "name": "App Name",
  "description": "Brief description of what the app does."
}
```

### Error Handling

- **400 Bad Request**: Invalid category parameter
- **500 Internal Server Error**: Error generating app idea

## Dependencies

- FastAPI
- Uvicorn
- OpenAI Agents
- Pydantic
- Other dependencies listed in `requirements.txt`

## Development

The application uses:

- **FastAPI** for the web framework
- **OpenAI Agents** for generating app ideas
- **Uvicorn** as the ASGI server
- **Pydantic** for data validation
- **CORS middleware** for cross-origin requests

## CORS Support

The API supports Cross-Origin Resource Sharing (CORS) to allow requests from web applications running on different domains or ports. The current configuration allows:

- **All origins** (`*`)
- **All HTTP methods** (GET, POST, PUT, DELETE, etc.)
- **All headers**
- **Credentials** (cookies, authorization headers)

This makes the API suitable for frontend applications running on different hosts or ports.

## License

This project is part of the "100 Vibe Apps in 100 Days" project.
