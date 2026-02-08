# Django Tools

A Django web application providing everyday utility tools -- password generation, live weather lookup, and QR code creation. Built with Django, Tailwind CSS, and Vite.

## Features

- **Password Generator** -- Customizable length (6-16), uppercase, digits, and symbols.
- **Weather Information** -- Real-time weather for any city via OpenWeatherMap (Celsius, Fahrenheit, Kelvin).
- **QR Code Generator** -- Create QR codes from any URL or text with custom size, colors, and error correction levels. Download as PNG or copy to clipboard.

## Prerequisites

- Python 3.1+
- Node.js 16+
- npm

## Installation

```bash
git clone https://github.com/NjauSamuel/Django-Password-Generator.git
cd Django-Password-Generator
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
npm install
npm run build
```

## Environment Variables

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

Get a free API key at [OpenWeatherMap](https://openweathermap.org/) (sign up, then visit [API Keys](https://home.openweathermap.org/api_keys)). It may take 10-60 minutes to activate.

## Running the Application

```bash
npm run build          # build frontend assets
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

For frontend development with auto-rebuild:

```bash
npm run dev
```

## Technologies

- **Backend**: Django 6.0, Python 3.1+, python-dotenv, requests
- **Frontend**: Tailwind CSS 4.1, Vite 7.3
- **APIs**: OpenWeatherMap
- **QR Code**: qrcodejs (client-side generation)

## Contributing

Contributions are welcome -- feel free to submit a Pull Request.

## License

ISC License

## Author

NjauSamuel
