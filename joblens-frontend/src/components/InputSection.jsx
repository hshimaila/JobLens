import { useState } from "react";

export default function InputSection({ jd, setJd, analyze, setResumeFile }) {
  const [fileName, setFileName] = useState("");

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setResumeFile(file);
    setFileName(file ? file.name : "");
  };

  return (
    <div className="grid gap-4 mt-6">

      {/* File Upload */}
      <div className="bg-white p-4 rounded-xl shadow-md">
        <label className="block font-semibold mb-2">
          Upload Resume (PDF/DOCX)
        </label>

        <input
          type="file"
          onChange={handleFileChange}
          className="w-full"
        />

        {fileName && (
          <p className="mt-2 text-sm text-gray-600">
            Selected: {fileName}
          </p>
        )}
      </div>

      {/* Job Description */}
      <textarea
        placeholder="Paste Job Description..."
        className="p-4 rounded-xl shadow-md w-full h-40"
        value={jd}
        onChange={(e) => setJd(e.target.value)}
      />

      {/* Button */}
      <div className="text-center">
        <button
          onClick={analyze}
          className="bg-blue-600 text-white px-6 py-2 rounded-xl hover:bg-blue-700 transition hover:scale-105"
        >
          Analyze Resume
        </button>
      </div>
    </div>
  );
}