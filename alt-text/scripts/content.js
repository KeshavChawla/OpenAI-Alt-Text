$(document).ready(function() {
    console.log("HELLO")
    $('img:not([alt]), img[alt=""]').each(function() {
        // TODO: call OpenAI API with image url of this.src
        $(this).attr('alt', 'OPENAI_DESC_RESULT')
    });
});
