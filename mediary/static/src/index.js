document.addEventListener('DOMContentLoaded', () => {
    if (!window.Geoapify) {
        console.error('Geoapify is not defined. Ensure the Geoapify CDN is loaded.');
        return;
    }

    const locationInput = document.getElementById('id_location');
    if (!locationInput) {
        console.error('Location input not found');
        return;
    }

    const autocomplete = new Geoapify.GeocoderAutocomplete(
        locationInput,
        'c528b03c952847678a2efe93445c4edf',
        {
            type: 'street',
            lang: 'en',
            limit: 5
        }
    );

    autocomplete.on('select', (value) => {
        if (value && value.properties) {
            const latInput = document.getElementById('latitude');
            const lonInput = document.getElementById('longitude');
            if (latInput && lonInput) {
                latInput.value = value.properties.lat;
                lonInput.value = value.properties.lon;
                console.log(`Selected: ${value.properties.formatted}, Lat: ${value.properties.lat}, Lon: ${value.properties.lon}`);
            } else {
                console.error('Latitude or Longitude input not found');
            }
        }
    });

    autocomplete.on('error', (error) => {
        console.error('Geoapify Autocomplete error:', error);
    });
});