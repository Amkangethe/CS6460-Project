// --------------------------------------------------------------------------------------
// Style tasks container
const tasks = {
    count_vowels: {
        concepts: ["strings", "loops", "conditionals"],
        description: "Count how many vowels appear in a given string."
    },
    dedupe: {
        concepts: ["lists", "sorting", "iteration"],
        description: "Remove repeated values from a list and keep only unique items."
    },
    fizzbuzz: {
        concepts: ["loops", "modulo", "conditionals"],
        description: "Return Fizz, Buzz, or FizzBuzz based on divisibility rules."
    },
    is_palindrome: {
        concepts: ["strings", "slicing", "comparison"],
        description: "Check whether a word or phrase reads the same backward."
    },
    letter_grade: {
        concepts: ["conditionals", "comparison ranges", "returning values"],
        description: "Convert a numeric score into its matching letter grade."
    },
    my_max: {
        concepts: ["lists", "iteration", "comparison"],
        description: "Find and return the largest value in a list."
    },
    reverse_words: {
        concepts: ["strings", "split()", "lists"],
        description: "Reverse the order of words in a string."
    },
    running_sum: {
        concepts: ["lists", "indexing", "accumulation"],
        description: "Build a list where each value is the sum up to that point."
    }
};

const taskDropdown = document.getElementById("task");
const taskInfo = document.getElementById("taskConcepts");

let conceptsHTML = '';
let descriptionsHTML = '';

taskDropdown.addEventListener("change", () => {
    const selectedTask = taskDropdown.value;
    const taskData = tasks[selectedTask];

    conceptsHTML = `Concepts: ${taskData.concepts.join(", ")}`;
    document.getElementById("taskConcepts").innerHTML = conceptsHTML;

    descriptionsHTML = `${taskData.description}`;
    document.getElementById("taskDescriptions").innerHTML = descriptionsHTML;

    document.getElementById("taskName").innerHTML = `Task: ${selectedTask}`;
});
// --------------------------------------------------------------------------------------
