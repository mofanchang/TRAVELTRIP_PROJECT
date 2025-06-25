import React, { useState } from "react";

export default function ChatWidget() {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState([
    { from: "bot", text: "請輸入想去的地方與天數，例如：東京三日遊,韓國六日親子行程,北海道溫泉行" },
  ]);
  const [input, setInput] = useState("");

  const toggleOpen = () => setOpen(!open);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { from: "user", text: input };
    setMessages((msgs) => [...msgs, userMsg]);
    setInput("");

    try {
      const res = await fetch("/chatbot/chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });
      const data = await res.json();

      if (data.recommended_trips && data.recommended_trips.length > 0) {
        const tripMsgs = data.recommended_trips.map((trip, i) => ({
          from: "bot",
          text: (
            <div key={i}>
              <div>
                {trip.name} 
              </div>
              <a href={trip.link} target="_blank" rel="noopener noreferrer">
                查看詳情
              </a>
            </div>
          ),
        }));
        setMessages((msgs) => [...msgs, ...tripMsgs]);
      } else {
        setMessages((msgs) => [...msgs, { from: "bot", text: "抱歉，找不到符合的行程。" }]);
      }
    } catch {
      setMessages((msgs) => [...msgs, { from: "bot", text: "伺服器錯誤，請稍後再試。" }]);
    }
  };

  return (
    <>
      {open && (
        <div
          style={{
            position: "fixed",
            bottom: 80,
            right: 20,
            width: 320,
            height: 400,
            boxShadow: "0 0 10px #ccc",
            borderRadius: 8,
            backgroundColor: "white",
            fontFamily: "Arial, sans-serif",
            display: "flex",
            flexDirection: "column",
            zIndex: 9999,
            overflow: "hidden",
          }}
        >
          <div
            style={{
              flex: 1,
              overflowY: "auto",
              padding: 10,
              borderBottom: "1px solid #ddd",
            }}
          >
            {messages.map((m, i) => (
              <div
                key={i}
                style={{
                  textAlign: m.from === "user" ? "right" : "left",
                  marginBottom: 8,
                }}
              >
                <span
                  style={{
                    display: "inline-block",
                    padding: "8px 12px",
                    borderRadius: 20,
                    backgroundColor: m.from === "user" ? "#0084ff" : "#eee",
                    color: m.from === "user" ? "white" : "black",
                    maxWidth: "80%",
                    whiteSpace: "pre-wrap",
                    wordBreak: "break-word",
                  }}
                >
                  {typeof m.text === "string" ? m.text : m.text}
                </span>
              </div>
            ))}
          </div>
          <div style={{ padding: 10, borderTop: "1px solid #ddd" }}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              style={{
                width: "80%",
                padding: 8,
                borderRadius: 4,
                border: "1px solid #ccc",
              }}
              placeholder="輸入訊息..."
            />
            <button
              onClick={sendMessage}
              style={{ width: "18%", marginLeft: "2%", cursor: "pointer" }}
            >
              送出
            </button>
          </div>
        </div>
      )}

      <button
        onClick={toggleOpen}
        style={{
          position: "fixed",
          bottom: 20,
          right: 20,
          width: 60,
          height: 60,
          borderRadius: "50%",
          backgroundColor: "#0084ff",
          border: "none",
          color: "white",
          fontSize: 30,
          cursor: "pointer",
          zIndex: 10000,
        }}
        title="旅遊小幫手"
      >
        💬
      </button>
    </>
  );
}
