import g4f

def gpt_handle(txt):
	response = g4f.ChatCompletion.create(
		        model=g4f.models.gpt_4,
		        provider=g4f.Provider.Bing,
		        messages=[{"role": "user", "content": f"{txt}"}],
		    )
		    
	return response
