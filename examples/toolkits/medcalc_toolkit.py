# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========

from camel.agents import ChatAgent
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import MedCalcToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = """You are a helpful assistant."""

# Set model config
tools = MedCalcToolkit().get_tools()
print(tools)
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# Define a user message with a complex expression
usr_msg = """A 30-year-old woman comes to the physician because of headaches and nausea for the past 3 weeks. The headaches are holocranial and last up to 
several hours. During this period, she has also had a swishing sound in both ears, which decreases when she turns her head to either side. 
She has had multiple episodes of blurring of vision and double vision for the past 2 weeks. She has vomited twice in the past week. 
She has nodular cystic acne and polycystic ovarian disease. Current medications include an oral contraceptive, metformin, and isotretinoin. 
She is 163 cm (5 ft 4 in) tall and weighs 89 kg (196 lb); BMI is 33.5 kg/m2. Her temperature is 37.3掳C (99.1掳F), pulse is 70/min, and blood 
pressure is 128/82 mm Hg. She is oriented to time, place, and person. Examination shows acne over her cheeks and back. Hirsutism is present. 
Visual acuity is 20/20 in both eyes. There is esotropia of the left eye.
Using the adjusted body weight formula, what is the patient's adjusted body weight in terms of kg?"""

# Get response information
response = camel_agent.step(usr_msg)
print(response.info['tool_calls'])
'''
===============================================================================
[ToolCallingRecord(tool_name='simplify_expression', args={'expression': '(x**4 
- 16)/(x**2 - 4) + sin(x)**2 + cos(x)**2 + (x**3 + 6*x**2 + 12*x + 8)/(x + 2)
'}, result='{"status": "success", "result": "2*x**2 + 4*x + 9"}', 
tool_call_id='call_CdoZsLWeagT0yBM13RYuz09W')]
===============================================================================
'''
