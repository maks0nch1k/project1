function handleImageUpload(event) {
    const image = document.getElementById('post-image');
    image.src = URL.createObjectURL(event.target.files[0]);
    image.style.display = 'block';
}

function Copy(containerid) {
	    let textarea = document.createElement('textarea');
	    textarea.id = 'temp';
	    textarea.style.height = 0;
	    document.body.appendChild(textarea);
	    textarea.value = document.getElementById(containerid).innerText;
	    let selector = document.querySelector('#temp');
	    selector.select();
	    document.execCommand('copy');
	    document.body.removeChild(textarea);
}