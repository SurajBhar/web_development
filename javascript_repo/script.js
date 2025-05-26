function greet(event)
        {
            let name = document.querySelector('#name').value;
            alert('hello, '+ name);
            event.preventDefault();
        }
        let form = document.querySelector('form');
        form.addEventListener('submit', greet);