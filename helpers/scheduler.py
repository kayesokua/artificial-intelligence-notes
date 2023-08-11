import random
import copy
from deap import base, creator, tools, algorithms

dance_styles = ['Ballet', 'Contemporary', 'Jazz', 'Graham-Based Modern', 'Body Conditioning', 'Choreography-Improvisation']

def generate_mock_instructors(size):
    mock_instructors = {}
    for i in range(1, size + 1):
        instructor_id = f'instructor_{i}'
        expertise = random.sample(dance_styles, 2)
        availability = random.sample(range(1, 6), 2)
        rate_per_hour = random.randint(55, 100)
        trust_score = round(random.uniform(2.5, 5), 1)
        mock_instructors[instructor_id] = {
            'expertise': expertise,
            'availability': availability,
            'rate_per_hour': rate_per_hour,
            'trust_score': trust_score
        }
    return mock_instructors

def generate_program_schedule(program_requirements):
    """
    This creates a schedule based on program requirements and defined constraint (no repeating subject in the same day)
    """
    proposed_program_schedule = {}
    program_days = [1, 2, 3, 4, 5]
    classes_to_schedule = []

    for dance_style, num_classes in program_requirements.items():
        for i in range(num_classes):
            classes_to_schedule.append(dance_style)

    while True:
        random.shuffle(classes_to_schedule)
        valid_schedule = True
        for day in program_days:
            day_classes = set()
            day_classes.add(classes_to_schedule.pop())
            day_classes.add(classes_to_schedule.pop())
            if len(day_classes) < 2:
                valid_schedule = False
                return generate_program_schedule(program_requirements)
            proposed_program_schedule[day] = day_classes
        if valid_schedule:
            break

    return proposed_program_schedule

def recommend_instructors_based_on_schedule(schedule, candidates):
    instructors_scores = {}
    for instructor, values in data.items():
        instructors_scores[instructor] = sum(values['trust_score'].values())

    top2_experts = {}
    for day, classes in schedule.items():
        top2_experts[day] = {}
        for dance_style in classes:
            available_instructors = [(k, v) for k, v in data.items() if dance_style in v['expertise'] and day in v['availability']]
            if available_instructors:
                instructors_scores_subset = {k: v for k, v in instructors_scores.items() if k in [i[0] for i in available_instructors]}
                instructors_ranking = sorted(available_instructors, key=lambda x: instructors_scores_subset[x[0]], reverse=True)[:2]
                top2_experts[day][dance_style] = [instructor[0] for instructor in instructors_ranking]

    total_trust_score = 0
    for k, v in top2_experts.items():
        for k1, v1 in v.items():
            total_trust_score += sum([instructors_scores[i] for i in v1])

    return top2_experts, round(total_trust_score,2)