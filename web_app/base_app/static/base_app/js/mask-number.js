document.addEventListener('DOMContentLoaded', () => {

    const inputElement = document.getElementById('phone-number-input') // ищем наш единственный input
    const maskOptions = { // создаем объект параметров
      mask: '+{7}(000)000-00-00' // задаем единственный параметр mask
    }
    IMask(inputElement, maskOptions) // запускаем плагин с переданными параметрами
  
  })


    function confirmEmail() {
        var email = document.getElementById("email").value
        var confemail = document.getElementById("confemail").value
        if(email != confemail) {
            alert('Email Not Matching!');
        }
    }
</script>