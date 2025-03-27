function getData() {
    fetch("/api")
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error("Error fetching data:", error));
}
