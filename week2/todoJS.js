
// Логика закр конпки
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

// логика выбора
var list = document.querySelector("ul");
list.addEventListener("click", function(ev) {
  if (ev.target.tagName == "li") {
    ev.target.classList.className("checked");
  }
}, false);

// логика добавления
function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("Input_ID").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    // ничего не делаем
  } else {
    document.getElementById("UL_ID").appendChild(li);
  }
  document.getElementById("Input_ID").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("x");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}