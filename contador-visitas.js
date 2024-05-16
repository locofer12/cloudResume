
const counter = document.querySelector(".contador-visitas");
async function updateCounter() {
    let response = await fetch(
        "https://qlwzpwrohr7etkhiwt2pua2s2i0yaqkn.lambda-url.us-east-1.on.aws/"
    );
    let data = await response.json();
    counter.innerHTML = `Views: ${data}`;
}
updateCounter();