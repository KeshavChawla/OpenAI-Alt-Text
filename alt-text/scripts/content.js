function openai_get_alt_text(image_url, apiKey) {
    const url = "https://api.openai.com/v1/chat/completions";
    // const model = "gpt-3.5-turbo"
    const model = "gpt-4-vision-preview"
    messages = [
        {
            "role": "system",
            "content": "You are an assistant to help provide alt-text descriptions for images on websites missing these alt-text attributes.."
        },
        {

            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Generate an alt-text description for this image.",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    },
                }
            ]
        },
    ]

    const data = { model, messages }
    return fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${apiKey}`
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
      .catch(error => console.error('Error:', error));
}

$(document).ready(async function () {
    OPEN_AI_API_KEY = null
    await chrome.storage.local.get(["apiKey"]).then((result) => {
        $("#apiKey").val(result.apiKey);
        OPEN_AI_API_KEY = result.apiKey
    });

    $('img:not([alt]), img[alt=""]').each(async function () {
        res = await openai_get_alt_text(this.src, OPEN_AI_API_KEY);
        $(this).attr('alt', res.choices[0].message.content)
    });
});
