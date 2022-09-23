function goHome() {
    window.location = window.location.href.split('/pages')[0] + '/index.html';
}

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