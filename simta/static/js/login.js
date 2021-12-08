var myModal = document.getElementById('loginModal')
var myInput = document.getElementById('loginModal')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})