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
      alert("Please upload resume and enter job description");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_description", jd);

    try {
      const res = await fetch("http://127.0.0.1:8000/api/analyze/", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="bg-gray-100 min-h-screen">

      <Navbar />

      <div className="p-6 max-w-5xl mx-auto">

        <InputSection
          jd={jd}
          setJd={setJd}
          analyze={analyze}
          setResumeFile={setResumeFile}
        />

        {loading && (
          <p className="text-center mt-4 text-gray-600">
            Analyzing your resume...
          </p>
        )}

        {result && <ResultCard result={result} />}

        {/* Suggestions (later connect backend) */}
        {result && <Suggestions suggestions={result.suggestions} />}
      </div>
    </div>
  );
}