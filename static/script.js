function showLoading() {

    document.getElementById("loading").style.display = "block";

    document.querySelector("button").disabled = true;

    document.querySelector("button").innerText = "Uploading...";

}