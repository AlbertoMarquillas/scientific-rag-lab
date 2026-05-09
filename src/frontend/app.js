const uploadForm = document.getElementById("upload-form");
const fileInput = document.getElementById("pdf-file");
const dropzone = document.getElementById("dropzone");
const fileInfo = document.getElementById("file-info");
const uploadOutput = document.getElementById("upload-output");
const uploadButton = document.getElementById("upload-button");

const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");
const chatButton = document.getElementById("chat-button");
const chatMessages = document.getElementById("chat-messages");

let hasUploadedDocument = false;

function setUploadOutput(data, type = "") {
  uploadOutput.className = `output ${type}`;
  uploadOutput.textContent =
    typeof data === "string" ? data : JSON.stringify(data, null, 2);
}

function addMessage(role, content, extraClass = "") {
  const message = document.createElement("div");
  message.className = `message ${role} ${extraClass}`.trim();
  message.textContent = content;
  chatMessages.appendChild(message);
  chatMessages.scrollTop = chatMessages.scrollHeight;
  return message;
}

function updateFileInfo(file) {
  if (!file) {
    fileInfo.classList.add("hidden");
    fileInfo.textContent = "";
    return;
  }

  const sizeMb = (file.size / 1024 / 1024).toFixed(2);
  fileInfo.classList.remove("hidden");
  fileInfo.textContent = `Selected: ${file.name} (${sizeMb} MB)`;
}

function validatePdf(file) {
  if (!file) {
    throw new Error("Please select a PDF file.");
  }

  if (file.type !== "application/pdf" && !file.name.toLowerCase().endsWith(".pdf")) {
    throw new Error("Only PDF files are supported.");
  }
}

fileInput.addEventListener("change", () => {
  updateFileInfo(fileInput.files[0]);
});

dropzone.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropzone.classList.add("dragover");
});

dropzone.addEventListener("dragleave", () => {
  dropzone.classList.remove("dragover");
});

dropzone.addEventListener("drop", (event) => {
  event.preventDefault();
  dropzone.classList.remove("dragover");

  const file = event.dataTransfer.files[0];

  if (!file) {
    return;
  }

  fileInput.files = event.dataTransfer.files;
  updateFileInfo(file);
});

uploadForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const file = fileInput.files[0];

  try {
    validatePdf(file);

    const formData = new FormData();
    formData.append("file", file);

    uploadButton.disabled = true;
    uploadButton.textContent = "Uploading...";
    setUploadOutput("Uploading PDF and starting ingestion...");

    const response = await fetch("/api/documents/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Upload failed.");
    }

    hasUploadedDocument = true;

    setUploadOutput(data, "success");

    addMessage(
      "assistant",
      `PDF uploaded: ${data.file_name}\nYou can now ask questions about it.`
    );
  } catch (error) {
    setUploadOutput(error.message, "error");
    addMessage("assistant", `Upload error: ${error.message}`, "error");
  } finally {
    uploadButton.disabled = false;
    uploadButton.textContent = "Upload and ingest";
  }
});

chatForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (!hasUploadedDocument) {
    addMessage("assistant", "Please upload a PDF before asking questions.");
    return;
  }

  const query = chatInput.value.trim();

  if (!query) {
    return;
  }

  addMessage("user", query);
  chatInput.value = "";

  const loadingMessage = addMessage("assistant", "Thinking...");

  try {
    chatButton.disabled = true;

    const response = await fetch("/api/chat/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query,
        top_k: 5,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Query failed.");
    }

    loadingMessage.textContent = data.answer || "No answer returned.";
  } catch (error) {
    loadingMessage.classList.add("error");
    loadingMessage.textContent = `Error: ${error.message}`;
  } finally {
    chatButton.disabled = false;
    chatInput.focus();
  }
});