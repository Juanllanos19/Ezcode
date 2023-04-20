const JAVA_KEY = "62";
const CPP_KEY = "53";
const PYTHON_KEY = "70";
const BASE_URL = "https://judge0-ce.p.rapidapi.com/submissions";


function codeEditor(lang_id) {
  var editor = ace.edit("editor");
  editor.setTheme("ace/theme/twilight");

  console.log("id" + lang_id )
  $(document).ready(function () {
    $("button").click(function () {
      let code = editor.getValue();
      $("#ans").html("Loading...");
      console.log(code);
      let data = {
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
      };
      const options = {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'Content-Type': 'application/json',
          'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
          'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
        },
        body: '{"language_id":92,"source_code":"' + btoa(code) +'=","stdin":"SnVkZ2Uw"}'
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
          'X-RapidAPI-Key': '0ae7a38b45msh71c6a1fcbf098e2p1d5efbjsn3ccb076e28db',
          //'X-RapidAPI-Key': '9e626646d1mshd9fd0c9fed686ecp1bbed0jsn8815f340f24a',
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

      
      /*let request = $.ajax(
        {
        url: BASE_URL,
        type: "post",
        data: data,
      });*/
      /*
      const delay = (ms) => new Promise((res) => setTimeout(res, ms));
      // Callback handler that will be called on success
      request.done(async function (response, textStatus, jqXHR) {
        // Log a message to the console
        console.log("Hooray, it worked!");
        let token = response.token;
        await new Promise((resolve) => setTimeout(resolve, 3000)); // 3 sec
        console.log(3, "after 3 seconds");
        let second_request = $.ajax({
          url: BASE_URL + "/"+ token,
          type: "get",
        });
        second_request.done(function (response) {
          console.log(response.stdout);
          $("#ans").html(response.stdout);
        });
      });
      */
    });
  });
  if(lang_id==PYTHON_KEY)
      editor.setValue("def execute(): \n\t for i in range(10):\n\t\t print i \nexecute()")
  //java
  if(lang_id==JAVA_KEY){

      let javacode = `public class Main{
  public static void main(String args[]){
    System.out.println("hello");
  }
}
`;

  editor.setValue(javacode)

  }if(lang_id==CPP_KEY){
      let cppcode = `#include <iostream>
using namespace std;
  int main() {
      cout<<"Hello World"; \n
}`
      editor.setValue(cppcode)
  }


} 
