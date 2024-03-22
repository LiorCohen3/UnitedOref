
function initMiniMap(latitude, longitude, mapId) {
    const myLatLng = { lat: latitude, lng: longitude };
    const mapElement = document.getElementById(mapId);

    async function initializeMiniMap() {

        async try {
        const map = new google.maps.Map(mapElement, {
            zoom: 12,
            center: myLatLng
        });

        new google.maps.Marker({
            map: map,
            position: myLatLng,
            title: 'Your Location'
        });
        } catch (error) {
            console.error('Error initializing mini map:', error.message);
        }
    }

    initializeMiniMap();
}