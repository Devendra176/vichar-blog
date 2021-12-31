
    function showhide() {
      var div = document.getElementById("newpost");
      var div1 = document.getElementById("newpost1");
      var div2 = document.getElementById("newpost2");
      var div3 = document.getElementById("newpost3");
      var div4 = document.getElementById("newpost4");
      if (div.style.display !== "none") {
        div.style.display = "none";
      } else {
        div.style.display = "block";
        div1.style.display = "none";
        div2.style.display = "none";
        div3.style.display = "none";
        div4.style.display = "none";
      }
    }
 
    function showhide1() {
      var div = document.getElementById("newpost1");
      var div1 = document.getElementById("newpost");
      var div2 = document.getElementById("newpost2");
      var div3 = document.getElementById("newpost3");
      var div4 = document.getElementById("newpost4");
      if (div.style.display !== "none") {
        div.style.display = "none";
      } else {
        div.style.display = "block";
        div1.style.display = "none";
        div2.style.display = "none";
        div3.style.display = "none";
        div4.style.display = "none";
      }
    }

    function showhide2() {
      var div = document.getElementById("newpost2");
      var div1 = document.getElementById("newpost3");
      var div2 = document.getElementById("newpost1");
      var div3 = document.getElementById("newpost");
      var div4 = document.getElementById("newpost4");
      if (div.style.display !== "none") {
        div.style.display = "none";
      } else {
        div.style.display = "block";
        div1.style.display = "none";
        div2.style.display = "none";
        div3.style.display = "none";
        div4.style.display = "none";
      }
    }

    function showhide3() {
      var div = document.getElementById("newpost3");
      var div1 = document.getElementById("newpost2");
      var div2 = document.getElementById("newpost1");
      var div3 = document.getElementById("newpost");
      var div4 = document.getElementById("newpost4");

      if (div.style.display !== "none") {
        div.style.display = "none";
      } else {
        div.style.display = "block";
        div1.style.display = "none";
        div2.style.display = "none";
        div3.style.display = "none";
        div4.style.display = "none";
      }
    }

    function showhide4() {
      var div = document.getElementById("newpost4");
      var div1 = document.getElementById("newpost2");
      var div2 = document.getElementById("newpost1");
      var div3 = document.getElementById("newpost");
      var div4 = document.getElementById("newpost3");

      if (div.style.display !== "none") {
        div.style.display = "none";
      } else {
        div.style.display = "block";
        div1.style.display = "none";
        div2.style.display = "none";
        div3.style.display = "none";
        div4.style.display = "none";
      }
    }

    function readURL(input) {
  if (input.files && input.files[0]) {
  var reader = new FileReader();
  
  reader.onload = function (e) {
  $('#blah').attr('src', e.target.result).width(150).height(200);
  };
  
  reader.readAsDataURL(input.files[0]);
  }
  }
 




    function getFile() {
      document.getElementById("upfile").click();
    }
 
    function getFile1() {
      document.getElementById("upfile1").click();
    }

  function readURLpro(input){
  if (input.files && input.files[0]) {
  var reader = new FileReader();
  
  reader.onload = function (e) {
  $('#pro').attr('src', e.target.result).width(150).height(200);
  };
  
  reader.readAsDataURL(input.files[0]);
  }
  }
