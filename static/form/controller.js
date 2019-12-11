$(document).ready(function(){
    $("#form_92547").submit(function(event) {
        event.preventDefault()

        let patient = {
            bmi: $("#bmi").val(),
            age: $("#age").val(),
            glucose: $("#glucose").val(),
            insulin: $("#insulin").val(),
            skin_thickness: $("#skin").val(),
            pregnancies: $("#pregnancies").val(),
            blood_pressure: $("#blood_pressure").val(),
            diabetes_pedigree_func: $("#pedigree").val()
        }

        $.post("http://127.0.0.1:5000/predict", JSON.stringify(patient), function(response) {
             let answer_text = "Sua porcentagem de início de diabetes é: " + response.prediction.diabetes *  100 + "%"
             $("#answer").text(answer_text)
         })
    })
})