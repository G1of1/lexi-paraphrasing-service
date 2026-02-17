import json
from ai.gemini import client
import service.prompts as prompts


async def paraphrase_standard(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.standard_prompt(text)
        paraphrased_text = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        responseText = response.text
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                paraphrased_text = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"paraphrased_text": paraphrased_text, "success": True}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}


async def paraphrase_simplify(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.simplify_prompt(text)
        paraphrased_text = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt)
        responseText = response.text
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                paraphrased_text = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return { "paraphrased_text": paraphrased_text, "success": True}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}

async def paraphrase_shorten(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.shorten_prompt(text)
        paraphrased_text = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt)
        responseText = response.text
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                paraphrased_text = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"paraphrased_text": paraphrased_text, "success": True}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}

async def paraphrase_expand(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.expand_prompt(text)
        paraphrased_text = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt)
        responseText = response.text
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                paraphrased_text = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"paraphrased_text": paraphrased_text, "success": True}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}

async def paraphrase_academic(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.academic_prompt(text)
        paraphrased_text = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt)
        responseText = response.text
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                paraphrased_text = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"paraphrased_text": paraphrased_text, "success": True}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}

async def paraphrase_formal(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.formal_prompt(text)
        paraphrased_text = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt)
        responseText = response.text
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                paraphrased_text = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"paraphrased_text": paraphrased_text, "success": True}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}


