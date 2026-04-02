import { useState } from "react";

export default function InputSection({ jd, setJd, analyze, setResumeFile }) {
  const [fileName, setFileName] = useState("");

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setResumeFile(file);
    setFileName(file ? file.name : "");
  };

  return (
    <div className="space-y-4">
      <div className="grid md:grid-cols-2 gap-4">

        {/* Upload */}
        <div className="bg-white border border-gray-100 rounded-2xl p-5">
          <p className="text-xs font-medium text-gray-400 uppercase tracking-widest mb-3">
            Resume
          </p>
          <label htmlFor="resume-upload" className="cursor-pointer block">
            <div className="border-2 border-dashed border-gray-200 hover:border-blue-400 transition-colors rounded-xl p-6 text-center bg-gray-50">
              <div className="w-9 h-9 bg-blue-50 rounded-lg flex items-center justify-center mx-auto mb-3">
                <svg width="18" height="18" viewBox="0 0 20 20" fill="none">
                  <path d="M10 3v10M6 7l4-4 4 4M3 15h14" stroke="#185FA5"
                    strokeWidth="1.5" strokeLinecap="round"/>
                </svg>
              </div>
              <p className="text-sm font-medium text-gray-800">Click to upload PDF</p>
              <p className="text-xs text-gray-400 mt-1">or drag and drop here</p>
            </div>
          </label>
          <input
            id="resume-upload"
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={handleFileChange}
            className="hidden"
          />
          {fileName && (
            <p className="text-xs text-blue-600 font-medium mt-2">{fileName}</p>
          )}
        </div>

        {/* JD */}
        <div className="bg-white border border-gray-100 rounded-2xl p-5">
          <p className="text-xs font-medium text-gray-400 uppercase tracking-widest mb-3">
            Job Description
          </p>
          <textarea
            placeholder="Paste the job description here..."
            className="w-full h-36 border border-gray-200 focus:border-blue-400 outline-none rounded-xl p-3 text-sm resize-none bg-gray-50 text-gray-800 transition-colors"
            value={jd}
            onChange={(e) => setJd(e.target.value)}
          />
        </div>
      </div>

      {/* Button */}
      <button
        onClick={analyze}
        className="w-full py-3.5 bg-blue-600 hover:bg-blue-700 active:scale-99 text-white font-semibold rounded-xl text-sm tracking-wide transition-all"
      >
        Analyze Resume
      </button>
    </div>
  );
}