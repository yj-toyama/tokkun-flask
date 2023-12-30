function callAPI() {
    fetch('/api/helloworld')
        .then(response => response.json())
        .then(data => document.getElementById('apiResponse').innerText = data.message);
}
