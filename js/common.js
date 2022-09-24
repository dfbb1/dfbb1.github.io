function initFolder() {
    document.getElementById('hide-btn-left').addEventListener('click', function () {
        document.getElementById('nav').style.display = 'none';
        document.getElementById('content').style.width = '100%';

        document.getElementById('hide-btn-left').style.display = 'none';
        document.getElementById('hide-btn-right').style.display = 'block';
    })

    document.getElementById('hide-btn-right').addEventListener('click', function () {
        document.getElementById('nav').style.display = 'inline-block';
        document.getElementById('content').style.width = '75%';

        document.getElementById('hide-btn-left').style.display = 'block';
        document.getElementById('hide-btn-right').style.display = 'none';
    })
}

var colorList = ['#d96800', '#0031de', '#36c200', '#313131',
    '#5100c2', '#bb0300']