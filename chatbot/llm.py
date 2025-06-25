from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "Qwen/Qwen1.5-0.5B-Chat"

print("正在載入模型...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map="cpu"
).eval()


def query_llm_local(user_input):
    system_prompt = (
    "你是一位旅遊推薦助理。請根據使用者輸入，"
    "忠實擷取輸入中的資訊並輸出 JSON 格式，如："
    "{\"天數\": 3, \"國家\": \"日本\", \"城市\": \"東京\", \"特徵\": \"美食, 景點\"}。\n"
    "輸入中出現的城市與國家名稱請優先使用，"
    "不得自行判斷替代地點，也不能添加多餘描述。"
)

   
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    try:
        inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)
        with torch.no_grad():
            outputs = model.generate(inputs.to("cpu"), max_new_tokens=256, do_sample=True)
        result = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)

        # 擷取 JSON 部分
        start = result.find("{")
        end = result.rfind("}")
        if start != -1 and end != -1:
            result = result[start:end+1]

        print("LLM 回傳：", result)
        return result

    except Exception as e:
        print("LLM 發生錯誤：", e)
        return '{"天數": 0, "國家": "", "城市": "", "特徵": ""}'
