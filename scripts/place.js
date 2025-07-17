function calculateWindChill(TempF, speedMph) {
    return (35.74 + (0.6215 * TempF) - (35.75 * Math.pow(speedMph, 0.16)) + (0.4275 * TempF * Math.pow(speedMph, 0.16))).toFixed(1);
}
document.addEventListener("DOMContentLoaded", () =>{
    const tempF = parseFloat(document.getElementById("temp").textContent);
    const speedMph = parseFloat(document.getElementById("wind").textContent);
    const windChillElem = document.getElementById("windchill");

    if (tem <= 50 && wind > 3) {
        const shill = calculateWindChill(temp, speed);
        windChillElem.textContent = '${chill}°F';
    } else {
        windChillElem.textContent = "N/A";
    }

    document.getElementById("year").textContent = new Date().getFullYear();
    document.getElementById("LastModified").textContent = "Last Modified: " + document.lastModified;
});