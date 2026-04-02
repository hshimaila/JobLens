import { useState } from "react";
import Navbar from "../components/Navbar";
import InputSection from "../components/InputSection";
import ResultCard from "../components/ResultCard";
import Suggestions from "../components/Suggestions";

export default function Dashboard() {
  const [jd, setJd] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [resumeFile, setResumeFile] = useState(null);

  const analyze = async () => {
    if (!resumeFile || !jd) {
      alert("Please upload a resume and enter a job description");
      return;
    }
    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_description", jd);

    const fetchWithRetry = async (retries = 3) => {
      for (let i = 0; i < retries; i++) {
        try {
          const controller = new AbortController();
          const timeout = setTimeout(() => controller.abort(), 90000); // 90 sec timeout
          const res = await fetch("https://joblens-backend-zbxo.onrender.com/api/analyze/", {
            method: "POST",
            body: formData,
            signal: controller.signal,
          });
          clearTimeout(timeout);
          return await res.json();
        } catch (err) {
          if (i === retries - 1) throw err;
          await new Promise(r => setTimeout(r, 3000)); // wait 3s before retry
        }
      }
    };

    try {
      const data = await fetchWithRetry();
      setResult(data);
    } catch (err) {
      console.error(err);
      alert("Server is taking too long to respond. Please try again in a moment.");
    }
    setLoading(false);
  };

  return (
    <div className="bg-gray-50 min-h-screen" style={{ fontFamily: "'DM Sans', sans-serif" }}>
      <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Syne:wght@700;800&display=swap" rel="stylesheet" />
      <Navbar />
      <div className="max-w-3xl mx-auto px-4 py-10">

        {/* Hero */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-black tracking-tight text-gray-900 mb-2"
            style={{ fontFamily: "'Syne', sans-serif" }}>
            Match your resume to any job
          </h1>
          <p className="text-sm text-gray-500">
            Upload your resume and paste a job description for an instant AI-powered skill gap analysis.
          </p>
        </div>

        <InputSection
          jd={jd}
          setJd={setJd}
          analyze={analyze}
          setResumeFile={setResumeFile}
        />

        {loading && (
          <div className="text-center mt-8 text-sm text-gray-400">
            Analyzing your resume
            <span className="inline-block animate-bounce mx-0.5">.</span>
            <span className="inline-block animate-bounce mx-0.5" style={{ animationDelay: "0.2s" }}>.</span>
            <span className="inline-block animate-bounce mx-0.5" style={{ animationDelay: "0.4s" }}>.</span>
          </div>
        )}

        {result && <ResultCard result={result} />}
        {result && <Suggestions suggestions={result.suggestions} />}
      </div>
    </div>
  );
}