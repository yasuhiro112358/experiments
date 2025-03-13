# dotenv
- Load environment variables from a `.env` file.

```python
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Access environment variables
api_key=os.environ.get("OPENAI_API_KEY"),
```