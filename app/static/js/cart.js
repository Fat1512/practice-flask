async function addToCart(id, name, price) {
    event.preventDefault();
    const res = await fetch('/api/cart', {
        method: 'POST',
        body: JSON.stringify({
            id: id,
            name: name,
            price: price
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await res.json();
    console.log(data)
    const counter = document.querySelector(".counter_element");
    counter.innerText = data.total_item;
}