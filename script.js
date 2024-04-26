function toggleVisibility() {
    var loginScreen = document.getElementById('login-screen');
    var imageRecognitionScreen = document.getElementById('image-recognition-screen');
    
    if (loginScreen.style.display !== 'none') {
        loginScreen.style.display = 'none';
        imageRecognitionScreen.style.display = 'flex';
    } else {
        loginScreen.style.display = 'flex';
        imageRecognitionScreen.style.display = 'none';
    }
}

function openFileBrowser() {
    document.getElementById('file-input').click();
}

document.getElementById('file-input').addEventListener('change', function() {
    if (this.files && this.files.length > 0) {
        alert('Archivo seleccionado: ' + this.files[0].name);
    }
});