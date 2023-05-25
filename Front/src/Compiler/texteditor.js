const JAVA_KEY = "62";
const CPP_KEY = "53";
const PYTHON_KEY = "70";
const BASE_URL = "https://judge0-ce.p.rapidapi.com/submissions";

var exercises;
var title;
var desc;

var problemid = 0;




function importJson(info)
{
    exercises = info;

    title = exercises[0].title;
    desc = exercises[0].description;
    $("#nombre").html(title);
    $("#descripcion").html(desc);
    console.log(exercises);
    fillDropdown();
}

function fillDropdown(){
  var sel = document.getElementById('myselect');
  for (var i = 0; i < exercises.length; i++)
  {
    var opt = document.createElement('option');
    opt.innerHTML = exercises[i].id;
    opt.value = i;
    sel.appendChild(opt);
  }
}

function changeId(num)
{
  problemid = num;
  $("#nombre").html(exercises[num].title);
  $("#descripcion").html(exercises[num].description);
}

