from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Optional
from webse.models import Userpage


class ChatFormUpdate(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

class ChatFormExercise(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

#M2_Ch1: SE, Frame.
class ModulsForm_m2_ch1_e1(FlaskForm):
    type = SelectField(validators=[DataRequired(False)],
                       choices=[('Should include only environmental pollution, carbon emissions', 'Should include only environmental pollution, carbon emissions'),
                                ('Should include only poverty alleviation, gender equality', 'Should include only poverty alleviation, gender equality'),
                                ('Should include both', 'Should include both')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_e2(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Green Economy is more related to welfare and environmental economics', 'Green Economy is more related to welfare and environmental economics'),
                                ('Green Economy is more related to ecological economics', 'Green Economy is more related to ecological economics'),
                                ('Green Economy is more related to economics schools', 'Green Economy is more related to economics schools')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Should only consider carbon emissions', 'Should only consider carbon emissions'),
                                ('Should only consider electrification', 'Should only consider electrification'),
                                ('Should also consider social aspects', 'Should also consider social aspects')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Pollution is a negative externality', 'Pollution is a negative externality'),
                                ('Sustainability and economy are a subsystem of the ecosystem', 'Sustainability and economy are a subsystem of the ecosystem'),
                                ('Research and technology are fundamental parts of agriculture development', 'Research and technology are fundamental parts of agriculture development')])
    submit = SubmitField('Submit')

#M2_Ch2: SE. Ch2. Ecological Footprint and Biocapacity
class ModulsForm_m2_ch2_e1(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('The ecological footprint should be charged to Norway', 'The ecological footprint should be charged to Norway'),
                                ('The ecological footprint should be charged to Spain', 'The ecological footprint should be charged to Spain'),
                                ('The ecological footprint should be charged partially to both countries', 'The ecological footprint should be charged partially to both countries')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_e2(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Land to capture carbon emissions', 'Land to capture carbon emissions'),
                                ('Cropland, grazing land, fishing grounds, and forest products land', 'Cropland, grazing land, fishing grounds, and forest products land'),
                                ('All the previous types of lands', 'All the previous types of lands')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_e3(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Land to capture carbon emissions', 'Land to capture carbon emissions'),
                                ('Cropland', 'Cropland'),
                                ('Fishing grounds', 'Fishing grounds')])
    submit = SubmitField('Submit')


class ModulsForm_m2_ch2_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Biologically productive area it takes to satisfy the exporting demand', 'Biologically productive area it takes to satisfy the exporting demand'),
                                ('Biologically productive area it takes to satisfy the demands of people', 'Biologically productive area it takes to satisfy the demands of people'),
                                ('Biologically productive area it takes to satisfy the importing demand', 'Biologically productive area it takes to satisfy the importing demand')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Land and sea area available to provide the resources a population consumes and to absorb its wastes',
                                 'Land and sea area available to provide the resources a population consumes and to absorb its wastes'),
                                ('Land and sea area available for agriculture and fisheries',
                                 'Land and sea area available for agriculture and fisheries'),
                                ('Land area available for wildlife',
                                 'Land area available for wildlife')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Productive land required to absorb the carbon dioxide emissions',
                                'Productive land required to absorb the carbon dioxide emissions'),
                                ('Amount of carbon absorbed by oceans',
                                 'Amount of carbon absorbed by oceans'),
                                ('Both', 'Both')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Cropland, grazing land, fishing grounds (marine waters), forest, and built-up',
                                'Cropland, grazing land, fishing grounds (marine waters), forest, and built-up'),
                                ('Cropland, grazing land, fishing grounds (marine and inland waters), forest, and built-up',
                                 'Cropland, grazing land, fishing grounds (marine and inland waters), forest, and built-up'),
                                ('Cropland, grazing land, fishing grounds (marine and inland waters), and forest',
                                 'Cropland, grazing land, fishing grounds (marine and inland waters), and forest')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Reflect the relative productivity of a given land use type',
                                'Reflect the relative productivity of a given land use type'),
                                ('Reflect the relative productivity of cropland',
                                 'Reflect the relative productivity of cropland'),
                                ('Reflect the relative productivity of fishing grounds',
                                 'Reflect the relative productivity of fishing grounds')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Very suitable, suitable, moderately suitable, and marginally suitable',
                                'Very suitable, suitable, moderately suitable, and marginally suitable'),
                                ('Very suitable, suitable, marginally suitable, and not suitable',
                                 'Very suitable, suitable, marginally suitable, and not suitable'),
                                ('Very suitable, suitable, moderately suitable, marginally suitable, and not suitable',
                                 'Very suitable, suitable, moderately suitable, marginally suitable, and not suitable')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'In the 80s',
                                'In the 80s'),
                                ('In the 70s',
                                 'In the 70s'),
                                ('In the 90s',
                                 'In the 90s')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'It represents the 50%','It represents the 50%'),
                                ('It represents the 40%','It represents the 40%'),
                                ('It represents the 60%', 'It represents the 60%')])
    submit = SubmitField('Submit')

#M2_Ch3: SE. Ch3. Human Development for the Anthropocene
class ModulsForm_m2_ch3_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('At the beginning of the Agricultural Revolution 12.000–15.000 years ago',
                                 'At the beginning of the Agricultural Revolution 12.000–15.000 years ago'),
                                ('In 1945 after the detonation of the first atomic bomb',
                                 'In 1945 after the detonation of the first atomic bomb'),
                                ('At the beginning of the Industrial Revolution',
                                 'At the beginning of the Industrial Revolution')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_e2(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Carbon emissions', 'Carbon emissions'),
                                ('Ecological Footprint', 'Ecological Footprint'),
                                ('Both', 'Both')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch3_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('At the beginning of the Agricultural Revolution 12.000–15.000 years ago', 'At the beginning of the Agricultural Revolution 12.000–15.000 years ago'),
                                ('In 1945 after the detonation of the first atomic bomb', 'In 1945 after the detonation of the first atomic bomb'),
                                ('The debate about the starting date of the Antrophocene is still open', 'The debate about the starting date of the Antrophocene is still open')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Homogenization of flora and fauna',
                                 'Homogenization of flora and fauna'),
                                ('One species (humans) consuming 25–40 percent of land net primary productivity',
                                 'One species (humans) consuming 25–40 percent of land net primary productivity'),
                                ('Increasing impact of new technologies as the biosphere interacts with the technosphere',
                                 'Increasing impact of new technologies as the biosphere interacts with the technosphere'),
                                ('Increase in arid areas',
                                 'Increase in arid areas')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Those elements do not interact with humans, and do not determine the relations of power and culture',
                                'Those elements do not interact with humans, and do not determine the relations of power and culture'),
                                ('Those elements do not interact with humans, and determine the relations of power and culture',
                                 'Those elements do not interact with humans, and determine the relations of power and culture')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch3_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Chemical pollution, and ocean acidification',
                                'Chemical pollution, and ocean acidification'),
                                ('Freshwater use, and phosphorus cycle',
                                 'Freshwater use, and phosphorus cycle'),
                                ('Biodiversity loss, climate crisis, and nitrogen cycle',
                                 'Biodiversity loss, climate crisis, and nitrogen cycle')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('They are two independent imbalances that operate independently',
                                 'They are two independent imbalances that operate independently'),
                                ('They are two interdependent imbalances that reinforce each other',
                                 'They are two interdependent imbalances that reinforce each other')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'The cost of carbon in 2030 will be $75 per tonne of carbon dioxide in 2017 US dollars',
                                'The cost of carbon in 2030 will be $75 per tonne of carbon dioxide in 2017 US dollars'),
                                ('The cost of carbon in 2030 will be $50 per tonne of carbon dioxide in 2017 US dollars',
                                 'The cost of carbon in 2030 will be $50 per tonne of carbon dioxide in 2017 US dollars'),
                                ('The cost of carbon in 2030 will be $85 per tonne of carbon dioxide in 2017 US dollars',
                                 'The cost of carbon in 2030 will be $85 per tonne of carbon dioxide in 2017 US dollars')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Multiplying the HDI by the social cost of carbon emissions',
                                'Multiplying the HDI by the social cost of carbon emissions'),
                                ('Multiplying the HDI by the ecological footprint',
                                 'Multiplying the HDI by the ecological footprint'),
                                ('Multiplying the HDI by the arithmetic mean of carbon emissions and the ecological footprint',
                                 'Multiplying the HDI by the arithmetic mean of carbon emissions and the ecological footprint')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'The PHDI in country B is larger','The PHDI in country B is larger'),
                                ('The PHDI in country A is larger','The PHDI in country A is larger'),
                                ('The PHDI does not depend on carbon emissions', 'The PHDI does not depend on carbon emissions')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'It is increasing the gap with the HDI','It is increasing the gap with the HDI'),
                                ('It is closing the gap with the HDI','It is closing the gap with the HDI'),
                                ('The gap between both indexes remains the same', 'The gap between both indexes remains the same')])
    submit = SubmitField('Submit')

#M2_Ch4: SE. Ch4. Global Energy Transformation. A road map to 2050
class ModulsForm_m2_ch4_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Electric vehicles, introduction of renewable energy, and energy efficiency',
                                 'Electric vehicles, introduction of renewable energy, and energy efficiency'),
                                ('Electrification, introduction of renewable energy, and energy efficiency',
                                 'Electrification, introduction of renewable energy, and energy efficiency'),
                                ('Auto-consumption, biomass, and energy efficiency',
                                 'Auto-consumption, biomass, and energy efficiency')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Agricultural sector, car sector, steel sector and building sector',
                                 'Agricultural sector, car sector, steel sector and building sector'),
                                ('Power sector, car sector, chemical sector and building sector',
                                 'Power sector, car sector, chemical sector and building sector'),
                                ('Power sector, industry sector, transport sector and building sector',
                                 'Power sector, industry sector, transport sector and building sector')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch4_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Electric vehicles, introduction of renewable energy, and energy efficiency', 'Electric vehicles, introduction of renewable energy, and energy efficiency'),
                                ('Electrification, introduction of renewable energy, and energy efficiency', 'Electrification, introduction of renewable energy, and energy efficiency'),
                                ('Auto-consumption, biomass, and energy efficiency', 'Auto-consumption, biomass, and energy efficiency')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Agricultural sector, car sector, steel sector and building sector',
                                 'Agricultural sector, car sector, steel sector and building sector'),
                                ('Power sector, car sector, chemical sector and building sector',
                                 'Power sector, car sector, chemical sector and building sector'),
                                ('Power sector, industry sector, transport sector and building sector',
                                 'Power sector, industry sector, transport sector and building sector')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The 66% of the electricity will be produced by using renewable energy',
                                'The 66% of the electricity will be produced by using renewable energy'),
                                ('The 76% of the electricity will be produced by using renewable energy',
                                 'The 76% of the electricity will be produced by using renewable energy'),
                                ('The 86% of the electricity will be produced by using renewable energy',
                                 'The 86% of the electricity will be produced by using renewable energy')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('20% in the building sector, 33% in the industry sector, 22% in the transport sector',
                                '20% in the building sector, 33% in the industry sector, 22% in the transport sector'),
                                ('40% in the building sector, 33% in the industry sector, 22% in the transport sector',
                                 '40% in the building sector, 33% in the industry sector, 22% in the transport sector'),
                                ('20% in the building sector, 33% in the industry sector, 12% in the transport sector',
                                 '20% in the building sector, 33% in the industry sector, 12% in the transport sector')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Solar, wind, hydrogen and hydropower',
                                 'Solar, wind, hydrogen and hydropower'),
                                ('Solar, wind, bioenergy and hydropower',
                                 'Solar, wind, bioenergy and hydropower'),
                                ('Solar, wind, bioenergy and nuclear',
                                 'Solar, wind, bioenergy and nuclear')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                '1, Electric vehicles (EV); 2, biofuels heavy freight, for road, aviation and marine transport',
                                '1, Electric vehicles (EV); 2, biofuels heavy freight, for road, aviation and marine transport'),
                                ('1, Hydrogen for vehicles, and heavy freight; 2, biofuels for road, aviation and marine transport',
                                 '1, Hydrogen for vehicles, and heavy freight; 2, biofuels for road, aviation and marine transport'),
                                ('1, EV; 2, hydrogen for heavy freight; 3, biofuels for road, aviation and marine transport',
                                 '1, EV; 2, hydrogen for heavy freight; 3, biofuels for road, aviation and marine transport')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Bioenergy for industrial heat and processes',
                                'Bioenergy for industrial heat and processes'),
                                ('Hydrogen and direct use of electricity for industrial heat and processes',
                                 'Hydrogen and direct use of electricity for industrial heat and processes'),
                                ('Gas for industrial heat and processes',
                                 'Gas for industrial heat and processes')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Renewables for heating, and electricity; biogas for cooking; increase in efficiency','Renewables for heating, and electricity; biogas for cooking; increase in efficiency'),
                                ('Renewables for electricity; biogas for heating and cooking; smart meters','Renewables for electricity; biogas for heating and cooking; smart meters'),
                                ('Renewables for heating and electricity; smart meters', 'Renewables for heating and electricity; smart meters')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Electrification, and renewables','Electrification, and renewables'),
                                ('Investment, consumer expenditure, and trade','Investment, consumer expenditure, and trade'),
                                ('Digitalization and electric vehicles (EV)', 'Digitalization and electric vehicles (EV)')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Around 10% for a 2°C global warming and 15% for a 5°C global warming','Around 10% for a 2°C global warming and 15% for a 5°C global warming'),
                                ('Around 5% for a 2°C global warming and 20% for a 5°C global warming','Around 5% for a 2°C global warming and 20% for a 5°C global warming'),
                                ('Around 20% for a 2°C global warming and 35% for a 5°C global warming', 'Around 20% for a 2°C global warming and 35% for a 5°C global warming')])
    submit = SubmitField('Submit')

#M2_Ch5: SE. Ch5. Sustainable Energy. Wind Energy
class ModulsForm_m2_ch5_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('To minimize the weight of the turbine', 'To minimize the weight of the turbine'),
                                ('To cover as much surface as possible and simultaneously minimize the cost of production', 'To cover as much surface as possible and simultaneously minimize the cost of production'),
                                ('To cover as much surface as possible maximizing energy production', 'To cover as much surface as possible maximizing energy production')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('30%', '30%'),
                                ('35%', '35%'),
                                ('40%', '40%')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch5_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Mass of wind that pass through an area A divided by the square of wind speed', 'Mass of wind that pass through an area A divided by the square of wind speed'),
                                ('Mass of wind that pass through an area A multiplied by the square of wind speed', 'Mass of wind that pass through an area A multiplied by the square of wind speed'),
                                ('Mass of wind that pass through an area A multiplied by the wind speed', 'Mass of wind that pass through an area A multiplied by the wind speed')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Measures possible production', 'Measures possible production'),
                                ('Measures actual production', 'Measures actual production'),
                                ('Measures actual production relative to possible production', 'Measures actual production relative to possible production')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('45%', '45%'),
                                ('40%', '40%'),
                                ('50%', '50%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('49.3%', '49.3%'),
                                ('59.3%', '59.3%'),
                                ('51.3%', '51.3%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('30%', '30%'),
                                ('35%', '35%'),
                                ('40%', '40%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('8844 GW, 1000 GW', '8844 GW, 1000 GW'),
                                ('9944 GW, 900 GW', '9944 GW, 900 GW'),
                                ('5044 GW, 1000 GW', '5044 GW, 1000 GW')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('150 GW/yr, 25 GW/yr', '150 GW/yr, 25 GW/yr'),
                                ('200 GW/yr, 45 GW/yr', '200 GW/yr, 45 GW/yr'),
                                ('250 GW/yr, 40 GW/yr', '250 GW/yr, 40 GW/yr')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('400-600 USD/KW, 1000-2000 USD/KW', '400-600 USD/KW, 1000-2000 USD/KW'),
                                ('650-1000 USD/KW, 1400-2800 USD/KW', '650-1000 USD/KW, 1400-2800 USD/KW'),
                                ('200-400 USD/KW, 900-1800 USD/KW', '200-400 USD/KW, 900-1800 USD/KW')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.02-0.03 USD/KWh, 0.03-0.07 USD/KWh', '0.02-0.03 USD/KWh, 0.03-0.07 USD/KWh'),
                                ('0.05-0.07 USD/KWh, 0.08-0.1 USD/KWh', '0.05-0.07 USD/KWh, 0.08-0.1 USD/KWh'),
                                ('0.07-0.09 USD/KWh, 0.11-0.13 USD/KWh', '0.07-0.09 USD/KWh, 0.11-0.13 USD/KWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.07USD/KWh', '0.07 USD/KWh'),
                                ('0.09 USD/KWh', '0.09 USD/KWh'),
                                ('0.12 USD/KWh', '0.12 USD/KWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q11(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('22%-38%, 33%-40%', '22%-38%, 33%-40%'),
                                ('32%-58%, 43%-60%', '32%-58%, 43%-60%'),
                                ('15%-30%, 23%-33%', '15%-30%, 23%-33%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q12(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('6.06 M', '6.06 M'),
                                ('5.06 M', '4.06 M'),
                                ('4.06 M', '4.06 M')])
    submit = SubmitField('Submit')

#M2_Ch6: SE. Ch6. Sustainable Energy. Solar Energy
class ModulsForm_m2_ch6_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('25%', '25%'),
                                ('35%', '35%'),
                                ('30%', '30%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('From 0.37 USD/KWh to 0.085 USD/KWh', 'From 0.37 USD/KWh to 0.085 USD/KWh'),
                                ('From 0.12 USD/KWh to 0.09 USD/KWh', 'From 0.12 USD/KWh to 0.09 USD/KWh'),
                                ('From 0.17 USD/KWh to 0.095 USD/KWh', 'From 0.17 USD/KWh to 0.095 USD/KWh')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch6_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The cost has dropped from 0.5 $/KWh to 0.1-0.2 $/KWh', 'The cost has dropped from 0.5 $/KWh to 0.1-0.2 $/KWh'),
                                ('The cost has dropped from 0.5 $/KWh to 0.01-0.02 $/KWh', 'The cost has dropped from 0.5 $/KWh to 0.01-0.02 $/KWh'),
                                ('The cost has dropped from 0.5 $/KWh to 0.3-0.4 $/KWh', 'The cost has dropped from 0.5 $/KWh to 0.3-0.4 $/KWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The cost has dropped from 1160 $/KWh to 576 $/KWh', 'The cost has dropped from 1160 $/KWh to 576 $/KWh'),
                                ('The cost has dropped from 1160 $/KWh to 476 $/KWh', 'The cost has dropped from 1160 $/KWh to 476 $/KWh'),
                                ('The cost has dropped from 1160 $/KWh to 176 $/KWh', 'The cost has dropped from 1160 $/KWh to 176 $/KWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Non-concentrating collectors are used mainly at home, while concentrating collectors are used mainly in power plants', 'Non-concentrating collectors are used mainly at home, while concentrating collectors are used mainly in power plants'),
                                ('Both are mainly used at home', 'Both are mainly used at home'),
                                ('Both are mainly used in power plants', 'Both are mainly used in power plants')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('CSP is mainly used in the industry, while CST is mainly used in generation', 'CSP is mainly used in the industry, while CST is mainly used in generation'),
                                ('CST is mainly used in the industry, while CSP is mainly used in generation', 'CST is mainly used in the industry, while CSP is mainly used in generation'),
                                ('Both are mainly used in the industry', 'Both are mainly used in the industry')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.26', '0.26'),
                                ('0.36', '0.36'),
                                ('0.46', '0.46')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.1', '0.1'),
                                ('0.03', '0.03'),
                                ('0.15', '0.15')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Making the N-layer thick and heavily doped, and making the P-layer thick and heavily doped', 'Making the N-layer thick and heavily doped, and making the P-layer thick and heavily doped'),
                                ('Making the N-layer thin and heavily doped, and making the P-layer thick and heavily doped', 'Making the N-layer thin and heavily doped, and making the P-layer thick and heavily doped'),
                                ('Making the N-layer thin and heavily doped, and making the P-layer thick and poorly doped', 'Making the N-layer thin and heavily doped, and making the P-layer thick and poorly doped')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The combination of Amps and Ohms that maximize Watts', 'The combination of Amps and Ohms that maximize Watts'),
                                ('The combination of Amps and Volts that maximize Watts', 'The combination of Amps and Volts that maximize Watts'),
                                ('The combination of Ohms and Volts that maximize Watts', 'The combination of Ohms and Volts that maximize Watts')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('7000 GW', '7000 GW'),
                                ('7500 GW', '7500 GW'),
                                ('8500 GW', '8500 GW')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Asia 3000 GW, North-America 1300 GW, Europe 1200 GW, Africa 1000 GW', 'Asia 3000 GW, North-America 1300 GW, Europe 1200 GW, Africa 1000 GW'),
                                ('Asia 4800 GW, North-America 1720 GW, Europe 890 GW, Africa 670 GW', 'Asia 4800 GW, North-America 1720 GW, Europe 890 GW, Africa 670 GW'),
                                ('Asia 3500 GW, North-America 100 GW, Europe 1200 GW, Africa 1500 GW', 'Asia 3500 GW, North-America 100 GW, Europe 1200 GW, Africa 1500 GW')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q11(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('From 4621 USD/KW in 2010 to 481-165 USD/KW in 2050', 'From 4621 USD/KW in 2010 to 481-165 USD/KW in 2050'),
                                ('From 3000 USD/KW in 2010 to 1050-850 USD/KW in 2050', 'From 3000 USD/KW in 2010 to 1050-850 USD/KW in 2050'),
                                ('From 3500 USD/KW in 2010 to 1100-900 USD/KW in 2050', 'From 3500 USD/KW in 2010 to 1100-900 USD/KW in 2050')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q12(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.12 Euros/KWh', '0.12 Euros/KWh'),
                                ('0.16 Euros/KWh', '0.16 Euros/KWh'),
                                ('0.1 Euros/KWh', '0.1 Euros/KWh')])
    submit = SubmitField('Submit')
