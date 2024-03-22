
function initMiniMap(latitude, longitude, mapId) {
    const myLatLng = { lat: latitude, lng: longitude };
    const mapElement = document.getElementById(mapId);
    const map = new google.maps.Map(mapElement, {
         zoom: 12,
         center: myLatLng
    });

    new google.maps.Marker({
        map: map,
        position: myLatLng,
        title: 'Your Location'
    });
}