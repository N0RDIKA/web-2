function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const odj = {
        "method": drink,
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    };


    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(odj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        document.querySelector('#price').innerHTML = 'Цена напитка: ${data.result} руб';

    })
    };