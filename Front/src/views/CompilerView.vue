<script setup>
  // document.onload()

  function onSelectChange(selectedVal){
    console.log(selectedVal);
    if(selectedVal != undefined && selectedVal!=null && selectedVal!=""){
      changeId(selectedVal);
    }
  }
  fetch('./src/Compiler/testcases.json')
    .then(res => res.json())
    .then(data => importJson(data))


    function codeEditor(lang_id) {
      var editor = ace.edit("editor");
      editor.setTheme("ace/theme/twilight");

      var editor2 = ace.edit("editor2");
      editor2.setTheme("ace/theme/twilight");
      console.log("id:" + lang_id )
      $(document).ready(function () {
      $("button").click(function () {
    let code = editor.getValue();
    if (code == "")
    {
      console.log("esta vacio");
      $("#warning").html('<div class="alert alert-danger" role="alert"> ¡No hay codigo para correr! </div>');
    }
    else
    {
      console.log(code);
      $("#warning").html('');
      let input = editor2.getValue();
      $("#ans").html("Loading...");
      console.log(code);
      /*let data = {
        source_code: code,
        language_id: lang_id,
        number_of_runs: "1",
        stdin: "Judge0",
        expected_output: null,
        cpu_time_limit: "2",
        cpu_extra_time: "0.5",
        wall_time_limit: "5",
        memory_limit: "128000",
        stack_limit: "64000",
        max_processes_and_or_threads: "60",
        enable_per_process_and_thread_time_limit: false,
        enable_per_process_and_thread_memory_limit: false,
        max_file_size: "1024",
      };*/
      const options = {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'Content-Type': 'application/json',
          //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
          'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
          'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
        },
        body: '{"language_id":92,"source_code":"' + btoa(code) +'=","stdin":"' + btoa(input) + '", "redirect_stderr_to_stdout": true}'
      };

      
      async function retrieve(){fetch('https://judge0-ce.p.rapidapi.com/submissions?base64_encoded=true&fields=*', options)
        .then(response => response.json())
        .then(response => doubledown(response.token))
        //.then(response => console.log(response.token))
        .catch(err => console.error(err));
      }
      const options2 = {
        method: 'GET',
        headers: {
          //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
          'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
          'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
        }
      };
      
      async function doubledown(key){
        console.log(key);
        //console.log(key.token);
        fetch('https://judge0-ce.p.rapidapi.com/submissions/' + key + '?base64_encoded=true&fields=*', options2)
        .then(response => response.json())
        .then(response => changeOutput(response))
        .catch(err => console.error(err));
      }

      async function changeOutput(texto){
        if (texto.finished_at === null)
        {
          doudbledown(texto.token);
        }
        else{
          console.log(texto);
          console.log(texto.stdout);
          console.log(atob(texto.stdout));
          $("#ans").html(atob(texto.stdout));
        }
      }
      let request = retrieve();
    }


  });
  $("button2").click(function () {
    console.log("Boton2 activado");
    let code = editor.getValue();
    if (code == "")
    {
      console.log("esta vacio");
      $("#warning").html('<div class="alert alert-danger" role="alert"> ¡No hay codigo para correr! </div>');
    }
    else
    {
      $("#ans").html("Loading...");
      $("#warning").html('');

      var outputs = "---Tests---\n";

      var options = {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'Content-Type': 'application/json',
          //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
          'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
          'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
        },
        body: '{"language_id":92,"source_code":"' + btoa(code) +'=","stdin":"' + '' + '", "redirect_stderr_to_stdout": true}'
      };

      
      async function retrieve(){fetch('https://judge0-ce.p.rapidapi.com/submissions?base64_encoded=true&fields=*', options)
        .then(response => response.json())
        .then(response => doubledown(response.token))
        //.then(response => console.log(response.token))
        .catch(err => console.error(err));
      }
      const options2 = {
        method: 'GET',
        headers: {
          //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
          'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
          'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
        }
      };
      
      async function doubledown(key){
        console.log(key);
        //console.log(key.token);
        fetch('https://judge0-ce.p.rapidapi.com/submissions/' + key + '?base64_encoded=true&fields=*', options2)
        .then(response => response.json())
        .then(response => changeOutput(response))
        .catch(err => console.error(err));
      }

      async function changeOutput(texto){
        if (texto.finished_at === null)
        {
          await doudbledown(texto.token);
        }
        else{
          let inp = texto.stdin;
          let out = texto.stdout;
          let expectedOut = texto.expected_output;

          outputs = outputs + "Input: " + atob(inp) + "\n";
          outputs = outputs + "Output: " + atob(out);
          outputs = outputs + "Expected Output: " + atob(expectedOut);
          if (out == expectedOut)
          {
            outputs = outputs + "Result: SUCCESS" + "\n\n";
          }
          else
          {
            outputs = outputs + "Result: FAILED" + "\n\n";
          }
          console.log(outputs);
          $("#ans").html(outputs);
        }
      }

      async function test(num){
        options = {
          method: 'POST',
          headers: {
            'content-type': 'application/json',
            'Content-Type': 'application/json',
            //'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
            'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
            'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
          },
          body: '{"language_id":92,"source_code":"' + btoa(code) +'=","stdin":"' + btoa(exercises[problemid].tests[num].input) + '", "redirect_stderr_to_stdout": true, "expected_output": "' + btoa(exercises[problemid].tests[num].output) +'"}'
        };

        await retrieve();
      }

      async function runTests()
      {
        for (let i = 0; i < exercises[problemid].tests.length; i++)
        {
          console.log(exercises[problemid].tests[i].input);
          //outputs = outputs + "Test " + exercises[problemid].tests[i].testId + "\n";
          await test(i);
        }
      }
      runTests();
      //test(0);
    }
    

  });
});
editor.setValue('print("Hello world!")');
editor2.setValue("#Your inputs here");
$("#warning").html('');


} 


  window.onload = new function () {
    codeEditor("92");
  };
</script>

<template>
<html lang="en">
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
   <head>
    <meta charset="utf-8" />
    <title>EZcode</title>
    <link rel="stylesheet" type="text/css" href="./src/Compiler/assets/css/style.css" />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
      crossorigin="anonymous"
    />
   
  </head>
  <body>
    <div>
      <h1>EZcode</h1>
      <select id="myselect" onchange="onSelectChange(this.value.trim())"></select>
      <h2 id="nombre">Titulo</h2>
      <pre id="descripcion">Descripcion</pre>

      

      <div id="editorContainer">
        <div class="container" style="margin-top: 30px">
          <div class="row">
            <div class="col">
              <h3>Codigo</h3>
              <pre id="editor"></pre>
            </div>
            <div class="col">
              <h3>Inputs</h3>
              <pre id="editor2" style= "height: 150px; width: 200px"></pre>
              <div id="warning">
              </div>
              <button class="btn btn-success">Execute</button>
              <button2 class="btn btn-success">Test</button2>
              <br />
              <h3>Output</h3>
              <div class="scroll-box">
                <pre id="ans"></pre>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--<script type="module" src="src/mode-python.js"></script>-->

  </body>
</html>

</template>

<style type="text/css" media="screen">
      body {
        overflow: hidden;
      }

      #editor {
        min-width: 500px;
        min-height: 500px;
      }
</style>

