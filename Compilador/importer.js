

fetch('./testcases.json')
    .then(res => res.json())
    .then(data => importJson(data))


function importJson(info)
{
    var exercises = info;

    var title = exercises[0].title;
    var desc = exercises[0].description;
    $("#nombre").html(title);
    $("#descripcion").html(desc);
    console.log(exercises);
}
