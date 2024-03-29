function openai_get_alt_text(image_url, apiKey, includeColorDescription, extraDetailedDescription) {
  const openai_endpoint = "https://api.openai.com/v1/chat/completions";
  const openai_model = "gpt-4-vision-preview";
  messages = [
    {
      role: "system",
      content:
        "You are an assistant to help provide alt-text descriptions for images on websites missing these alt-text attributes. Generate and return back just an alt-text description for this image. Don't preface your answer with alt-text or any other indicator. Make sure that alt-text you provide follows the recommended guidelines for alt-text on the web.",
    },
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "Generate an alt-text description for this image.",
        },
        {
          type: "image_url",
          image_url: {
            url: image_url,
          },
        },
      ],
    },
  ];
  const api_call_data = { "model": openai_model, messages };
  return fetch(openai_endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify(api_call_data),
  })
    .then((res) => res.json())
    .catch((err) => console.error("OpenAI API Call Error:", err));
}

$(document).ready(async function () {
  OPENAI_API_KEY = null;
  OVERWRITE_ALT_TAGS = false;
  INCLUDE_COLOR_DESCRIPTION = false;
  EXTRA_DETAILED_DESCRIPTION = false;

  // get settings
  await chrome.storage.local.get(["apiKey"]).then((result) => {
    OPENAI_API_KEY = result.apiKey;
  });
  
  await chrome.storage.local.get(["overwriteAltTags"]).then((result) => {
    OVERWRITE_ALT_TAGS = result.apiKey;
  });
  
  await chrome.storage.local.get(["includeColorDescription"]).then((result) => {
    INCLUDE_COLOR_DESCRIPTION = result.apiKey;
  });
  
  await chrome.storage.local.get(["extraDetailedDescription"]).then((result) => {
    EXTRA_DETAILED_DESCRIPTION = result.apiKey;
  });

  $(OVERWRITE_ALT_TAGS ? 'img' : 'img:not([alt]), img[alt=""]').each(async function () {
    res = await openai_get_alt_text(this.src, OPENAI_API_KEY, INCLUDE_COLOR_DESCRIPTION, EXTRA_DETAILED_DESCRIPTION);
    $(this).attr("alt", res.choices[0].message.content);
  });
});
