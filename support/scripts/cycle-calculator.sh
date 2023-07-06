#!/bin/sh

CYCLE_DURATION_DAYS=45
# Real initial date is 2018-07-04 but because of manual miscalculations since that date, correct sequence was affected.
# Because of that start date will be the date of latest cycle before adding this script.
INITIAL_CYCLE_START_DATE_STRING='2023-05-16'

calculate_cycle_end_date() {
  # '-1 sec' is required to cover 23h and 59m of the cycle last day (and remove 46th day from the cycle).
  # Without it - end day will be on the 46th day right at midnight (12:00:00 AM).
  # Incrementing current date for 45 days (cycle duration) will add 45 days plus current day so it will be 46 days in
  # total. That's why we don't need to add extra 1 day before subtracting 1 second.
  date -d "${1} +${CYCLE_DURATION_DAYS} day -1 sec"
}

calculate_current_cycle() {
  # Since condition checks on dates strings is a bad idea - current date converted to timestamp.
  CURRENT_TIMESTAMP=$(date +%s)
  # Default initial cycle start date. Time should be 12:00:00 AM UTC so no format arguments added.
  # Overwritten for each cycle iteration.
  CYCLE_START_DATE=$(date -d "$INITIAL_CYCLE_START_DATE_STRING")
  # Empty variable which will hold current cycle normalized string on matching cycle star/end date relatively to
  # current date.
  CURRENT_CYCLE=

  # Iterate until finding the proper cycle start/end date relative to current date.
  while [ -z "${CURRENT_CYCLE}" ] ; do
    # Current iteration cycle start date converted to timestamp.
    CYCLE_START_DATE_TIMESTAMP=$(date -d "${CYCLE_START_DATE}" +%s)

    # Based on current iteration start date calculates the end date of the cycle.
    CYCLE_END_DATE=$(calculate_cycle_end_date "$CYCLE_START_DATE")

    # Current iteration cycle end date converted to timestamp.
    CYCLE_END_DATE_TIMESTAMP=$(date -d "${CYCLE_END_DATE}" +%s)

    [ "${CURRENT_TIMESTAMP}" -le "${CYCLE_END_DATE_TIMESTAMP}" ] && [ "${CURRENT_TIMESTAMP}" -ge "${CYCLE_START_DATE_TIMESTAMP}" ] && {
      # On matching current cycle interval - normalizes current cycle as a string.
      if [ "$(date -d "${CYCLE_START_DATE}" +%Y)" -eq "$(date -d "${CYCLE_END_DATE}" +%Y)" ];
        then
          CURRENT_CYCLE="$(date -d "${CYCLE_START_DATE}" +%b%-d)-$(date -d "${CYCLE_END_DATE}" +%b%-d-%Y)"
        else
          CURRENT_CYCLE="$(date -d "${CYCLE_START_DATE}" +%b%-d-%Y)-$(date -d "${CYCLE_END_DATE}" +%b%-d-%Y)"
      fi

      break
    }

    # Overwrites cycle start date with current iteration start date.
    CYCLE_START_DATE="$(date -d "${CYCLE_START_DATE} +${CYCLE_DURATION_DAYS} day")"
  done

  echo "$CURRENT_CYCLE"
}

# Calculates current cycle interval as a string.
calculate_current_cycle
