<script lang="ts">
	import { onMount } from 'svelte';
	import timezones from '../timezone.json';

	let time = '';
	let selectedTimeZone = 'Asia/Kolkata'; // Default to New York time
	let convertedTime = '';

	function getTimezoneOptions() {
		return timezones.map((timezone) => {
			return {
				label: timezone.text,
				value: timezone.utc[0]
			};
		});
	}

	function validate(time: string) {
		const regex = /^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9] (am|pm)$/i;
		return regex.test(time);
	}

	function getCurrentTime() {
		const now = new Date();
		let hours: any = now.getHours();
		const minutes = now.getMinutes().toString().padStart(2, '0');
		let amOrPm;

		if (hours === 12) {
			amOrPm = 'pm';
		} else {
			amOrPm = hours >= 12 ? 'pm' : 'am';
			hours = (hours % 12 || 12).toString().padStart(2, '0');
		}

		time = `${hours}:${minutes} ${amOrPm}`;
	}

	function convertTime() {
		if (!validate(time)) {
			alert('Invalid time format');
			return;
		}
		const inputTime = new Date(`2000-01-01 ${time}`);

		convertedTime = inputTime.toLocaleString('en-US', {
			timeZone: selectedTimeZone,
			hour12: true,
			hour: 'numeric',
			minute: 'numeric'
		});
	}
</script>

<main class="section has-text-centered">
	<h1 class="title">Clock Maker (v1)</h1>
	<p class="subtitle">Convert Indian time to any timezone you want</p>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css" />

	<section class="container is-desktop is-relative is-fullheight">
		<div class="field">
			<label class="label" for="time">Enter Time (HH:mm am/pm): </label>
			<div class="field is-grouped">
				<p class="control is-expanded">
					<input
						class="input is-fullwidth"
						type="text"
						placeholder="Enter time"
						id="time"
						bind:value={time}
					/>
				</p>
				<p class="control">
					<button class="button is-primary" on:click={getCurrentTime}>Now</button>
				</p>
			</div>
		</div>

		<div class="field">
			<label class="label" for="timezone">Select Timezone: </label>
			<div class="control">
				<div class="select is-fullwidth">
					<select class="input" id="timezone" bind:value={selectedTimeZone}>
						{#each getTimezoneOptions() as { label, value }}
							<option {value}>{label}</option>
						{/each}
					</select>
				</div>
			</div>
		</div>

		<div class="field">
			<div class="control">
				<button class="button is-primary" on:click={convertTime}>Convert Time</button>
			</div>
		</div>

		<div class="field">
			<p class="subtitle">Converted Time: {convertedTime}</p>
		</div>

		<p class="description is-absolute has-text-centered is-bottom-0">
			Made with ❤️ by <span><a href="https://github.com/0xrasla">rasla</a></span> for my beautiful wife
			Sorna
		</p>
	</section>
</main>
