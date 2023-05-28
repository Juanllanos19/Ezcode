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
              <div id="editor"></div>
            </div>
            <div class="col">
              <h3>Inputs</h3>
              <div id="editor2" style= "height: 150px; width: 200px"></div>
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

