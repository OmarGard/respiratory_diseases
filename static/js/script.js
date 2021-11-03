window.onload = function () {
    console.log('linked')
}
function selectModel(model) {
    console.log("clicked")
    if (model == 7) {
        document.getElementById('co2').style.display = 'block';
        document.getElementById('ch4').style.display = 'block';
        document.getElementById('n2o').style.display = 'block';
    }
    else {
        document.getElementById('co2').style.display = 'none';
        document.getElementById('ch4').style.display = 'none';
        document.getElementById('n2o').style.display = 'none';
    }
}